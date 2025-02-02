def debug_layout(widget, depth=0):
    """Recursively prints the layout structure, size policies, and geometry."""
    indent = "  " * depth  # Indentation for hierarchy

    # Get geometry
    geo = widget.geometry()
    size_policy = widget.sizePolicy()

    print(f"{indent}📌 {widget.__class__.__name__} ({widget.objectName()})")
    print(
        f"{indent}  Geometry: x={geo.x()}, y={geo.y()}, w={geo.width()}, h={geo.height()}"
    )
    print(
        f"{indent}  SizePolicy: H={size_policy.horizontalPolicy()}, V={size_policy.verticalPolicy()}"
    )
    print(
        f"{indent}  MinimumSize: {widget.minimumSize().width()}x{widget.minimumSize().height()}"
    )
    print(
        f"{indent}  MaximumSize: {widget.maximumSize().width()}x{widget.maximumSize().height()}"
    )
    print()

    # Check if the widget has a layout
    # layout = widget.layout
    # if layout:
    #     print(f"{indent}🔽 Layout: {layout.__class__.__name__}")
    #     for i in range(layout.count()):
    #         item = layout.itemAt(i)
    #         if item:
    #             child_widget = item.widget()
    #             if child_widget:
    #                 debug_layout(
    #                     child_widget, depth + 1
    #                 )  # Recursively check children
